import React, { useState } from 'react';
import { TextField, Button, Box, Paper } from '@mui/material';
import { motion } from 'framer-motion';
import SearchIcon from '@mui/icons-material/Search';

function FactForm({ onFetchFacts }) {
  const [url, setUrl] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onFetchFacts(url);
  };

  return (
    <Paper
      component={motion.form}
      initial={{ y: -20, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.5 }}
      elevation={3}
      onSubmit={handleSubmit}
      sx={{
        p: 3,
        borderRadius: 2,
        backgroundColor: 'rgba(255, 255, 255, 0.9)',
      }}
    >
      <Box sx={{ display: 'flex', gap: 2 }}>
        <TextField
          label="Enter URL"
          variant="outlined"
          fullWidth
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          required
          sx={{
            '& .MuiOutlinedInput-root': {
              '&:hover fieldset': {
                borderColor: 'primary.main',
              },
            },
          }}
        />
        <Button
          type="submit"
          variant="contained"
          color="primary"
          sx={{
            minWidth: '120px',
            borderRadius: 2,
            '&:hover': {
              transform: 'translateY(-2px)',
              transition: 'transform 0.2s ease-in-out',
            },
          }}
          startIcon={<SearchIcon />}
        >
          Get Facts
        </Button>
      </Box>
    </Paper>
  );
}

export default FactForm;