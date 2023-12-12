import React, { useContext, useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import Fade from '@mui/material/Fade';
import Divider from '@mui/material/Divider';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthProvider';

const Loading = ({ onLoad }) => {
  const navigate = useNavigate();
  const { setArtworks, setUsers } = useContext(AuthContext);
  const [sectionIndex, setSectionIndex] = useState(0);
  const [visible, setVisible] = useState(true);
  const sections = [
    'Welcome to <span style="color: #85144b;">Vignette</span>!',
    'Your <span style="color: #85144b;">Brushstroke</span> in the Digital Gallery of <span style="color: #85144b;">Expression</span>',
    '<span style="color: #85144b;">Vignette</span> (noun): a brief evocative description, account, or episode.'
  ];

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  const calculateTotalDuration = () => {
    const displayTime = 750; 
    return sections.length * displayTime;
  };

  useEffect(() => {
    const fetchDataAndNavigate = async () => {
      try {
        const artworksResponse = await fetch('/artworks');
        const artworkData = await artworksResponse.json();

        const usersResponse = await fetch('/users');
        const userData = await usersResponse.json();

        setArtworks(shuffleArray(artworkData));
        onLoad(shuffleArray(artworkData));
        setUsers(userData);

        await new Promise((resolve) => setTimeout(resolve, calculateTotalDuration()));

        navigate('/home');
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    let shuffledSections = shuffleArray(sections);
    let currentIndex = 0;

    setVisible(false);
    setTimeout(() => {
      setSectionIndex(currentIndex);
      setVisible(true);
      currentIndex++;
    }, 750);

    const interval = setInterval(() => {
      setVisible(false);

      setTimeout(() => {
        setSectionIndex(currentIndex);
        setVisible(true);

        currentIndex++;

        if (currentIndex === shuffledSections.length) {
          clearInterval(interval);
          setTimeout(fetchDataAndNavigate, calculateTotalDuration());
        }
      }, 500);
    }, calculateTotalDuration() + 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        height: '100vh',
        backgroundColor: 'black',
        color: 'white',
        fontSize: '75px',
        lineHeight: 1.5,
      }}
    >
      <Fade in={visible} timeout={250}>
        <div className='load-phrase' dangerouslySetInnerHTML={{ __html: sections[sectionIndex] }} />
      </Fade>
      <Divider sx={{ width: '20px' }} />
    </Box>
  );
};

export default Loading;
