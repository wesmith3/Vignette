import * as React from 'react'
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import MenuBar from './MenuBar';

const images = [
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  { img: '././Gallery.jpg', title: 'Title 1', author: 'Author 1' },
  { img: '././Gallery.jpg', title: 'Title 2', author: 'Author 2' },
  // Add more images as needed
]

const Gallery = () => {
  return (
    <>
      <MenuBar />
      <br />
      <div className='artist-plaque'/>
      <br />
      <div>
        <Box sx={{ width: '100%' }}>
          <ImageList variant="woven" cols={3} gap={0}>
            {images.map((item) => (
              <ImageListItem key={item.img} sx={{ margin: 5 }}>
                <img className='artwork' src={item.img} alt={item.title} loading="lazy" />
              </ImageListItem>
            ))}
          </ImageList>
        </Box>
        <br />
      </div>
    </>
  )
}

export default Gallery
