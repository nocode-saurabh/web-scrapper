import React from 'react';
import { motion } from 'framer-motion';
import { Typography, Paper } from '@mui/material';
import { useInView } from 'react-intersection-observer';

const AnimatedFact = ({ fact, index }) => {
  const [ref, inView] = useInView({
    triggerOnce: true,
    threshold: 0.1,
  });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, x: -20 }}
      animate={inView ? { opacity: 1, x: 0 } : { opacity: 0, x: -20 }}
      transition={{ duration: 0.5, delay: index * 0.1 }}
    >
      <Paper
        elevation={2}
        sx={{
          p: 2,
          mb: 2,
          borderRadius: 2,
          backgroundColor: 'rgba(255, 255, 255, 0.9)',
          '&:hover': {
            transform: 'scale(1.01)',
            transition: 'transform 0.2s ease-in-out',
          },
        }}
      >
        <Typography variant="body1">
          {fact}
        </Typography>
      </Paper>
    </motion.div>
  );
};

export default AnimatedFact;