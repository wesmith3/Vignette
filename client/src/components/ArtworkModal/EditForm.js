import { useState } from 'react';

function EditForm({ artwork, setIsEditing }) {
  const [editedArtwork, setEditedArtwork] = useState({
    title: artwork.title,
    description: artwork.description,
    price: artwork.price,
    tags: artwork.tags,
  })

  const handleEditSubmit = async (e) => {
    e.preventDefault()
    try {
      const flattenedPayload = {
        id: artwork.id,
        title: editedArtwork.title,
        description: editedArtwork.description,
        price: editedArtwork.price,
        tags: editedArtwork.tags.map((tag) => ({ ...tag, ...tag[0] })),
      }
  
      const response = await fetch(`/artworks/${artwork.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(flattenedPayload),
      })
  
      if (response.ok) {
        setIsEditing(false)
      } else {
        console.error('Error updating artwork:', response.statusText)
      }
    } catch (error) {
      console.error('Fetch error:', error)
    }
  }
  

  return (
    <form onSubmit={handleEditSubmit}>
            <label>
              Title:
              <input
                type='text'
                value={editedArtwork.title}
                onChange={(e) => setEditedArtwork({ ...editedArtwork, title: e.target.value })}
                placeholder='Title'
              />
            </label>
            <label>
              Description:
              <textarea
                value={editedArtwork.description}
                onChange={(e) => setEditedArtwork({ ...editedArtwork, description: e.target.value })}
                placeholder='Description'
              />
            </label>
            <label>
              Price:
              <input
                type='number'
                value={editedArtwork.price}
                onChange={(e) => setEditedArtwork({ ...editedArtwork, price: e.target.value })}
                placeholder='Price'
              />
            </label>
            <button type='submit'>Save Changes</button>
          </form>
  );
}

export default EditForm;
