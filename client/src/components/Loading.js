import React, { useContext, useEffect, useState } from 'react';
import { Transition, Divider } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from './AuthProvider';

const Loading = ({ onLoad }) => {
  const navigate = useNavigate();
  const { setArtworks, setUsers } = useContext(AuthContext);
  const [section, setSection] = useState(0);
  const [visible, setVisible] = useState(true);
  const sections = [
    'Welcome!',
    'Vignette: noun',
    'a brief evocative description, account, or episode.',
  ];

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }

  useEffect(() => {
    const fetchDataAndNavigate = async () => {
      try {
        // Fetch artworks
        const artworksResponse = await fetch('/artworks');
        const artworkData = await artworksResponse.json();

        // Fetch users
        const usersResponse = await fetch('/users');
        const userData = await usersResponse.json();

        // Set data in AuthProvider context
        setArtworks(shuffleArray(artworkData));
        onLoad(shuffleArray(artworkData));
        setUsers(userData);

        // Wait for 5 seconds (5000 milliseconds)
        await new Promise((resolve) => setTimeout(resolve, 3000));

        // Navigate to Home.js
        navigate('/home');
      } catch (error) {
        console.error('Error fetching data:', error);
        // Handle error, e.g., redirect to an error page
      }
    };

    const interval = setInterval(() => {
      setVisible(false);
      setSection((prevSection) => (prevSection + 1) % sections.length);
      setTimeout(() => {
        setVisible(true);
      }, 500); // Duration of the Transition animation
    }, 1500); // Duration for each section

    // Clear the interval after 5 seconds
    setTimeout(() => {
      clearInterval(interval);
      fetchDataAndNavigate(); // Call fetchDataAndNavigate after the loading phrases are displayed
    }, 5000);

    // Clean up the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <Transition visible={visible} animation='scale' duration={500}>
        <div>
          <h1>{sections[section]}</h1>
        </div>
      </Transition>
      <Divider hidden />
    </div>
  );
};

export default Loading;

