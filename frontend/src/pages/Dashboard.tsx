import { Box, Typography, Paper } from "@mui/material";
import React from "react";

export default function Dashboard() {
  return (
    <Paper elevation={3} sx={{ p: 3, maxWidth: 600, mx: "auto", mt: 8 }}>
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Box>
        <Typography variant="body1">Dashboard placeholder</Typography>
      </Box>
    </Paper>
  );
}
