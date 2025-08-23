import React, { useState } from 'react';
import { Box, Typography, Container, Alert } from '@mui/material';
import { motion, AnimatePresence } from 'framer-motion';
import { PacmanLoader } from 'react-spinners';
import FactForm from './FactForm';
import AnimatedFact from './AnimatedFact';
import config from './config';

function FactDisplay() {
  const [facts, setFacts] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchFacts = async (url) => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(`${config.API_URL}/scrape`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch facts');
      }

      const data = await response.json();
      setFacts(data);
    } catch (err) {
      setError(err.message);
      setFacts(null);
    } finally {
      setLoading(false);
    }
  };

  const factsList = facts?.facts.split('\n').filter(fact => fact.trim());

  return (
    <Container maxWidth="md">
      <Box
        sx={{
          minHeight: '100vh',
          py: 4,
          display: 'flex',
          flexDirection: 'column',
          gap: 4,
        }}
      >
        <motion.div
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <Typography
            variant="h4"
            component="h1"
            align="center"
            sx={{
              mb: 3,
              background: 'linear-gradient(45deg, #2196f3 30%, #21CBF3 90%)',
              backgroundClip: 'text',
              textFillColor: 'transparent',
              fontWeight: 'bold',
            }}
          >
            Factopedia
          </Typography>
        </motion.div>

        <FactForm onFetchFacts={fetchFacts} />

        <AnimatePresence>
          {loading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              style={{
                display: 'flex',
                justifyContent: 'center',
                padding: '2rem',
              }}
            >
              <PacmanLoader color="#2196f3" size={25} />
            </motion.div>
          )}

          {error && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
            >
              <Alert severity="error" sx={{ mt: 2 }}>
                {error}
              </Alert>
            </motion.div>
          )}

          {facts && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
            >
              <Typography
                variant="h5"
                component="h2"
                sx={{ mb: 3, fontWeight: 'medium' }}
              >
                {facts.title}
              </Typography>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                {factsList?.map((fact, index) => (
                  <AnimatedFact key={index} fact={fact} index={index} />
                ))}
              </Box>
            </motion.div>
          )}
        </AnimatePresence>
      </Box>
    </Container>
  );
}

export default FactDisplay;