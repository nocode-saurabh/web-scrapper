import React from 'react';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { theme } from './theme';
import FactDisplay from './FactDisplay';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <FactDisplay />
    </ThemeProvider>
  );
}

export default App;