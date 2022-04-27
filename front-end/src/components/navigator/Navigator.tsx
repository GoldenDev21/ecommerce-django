import {
  AppBar,
  Box,
  Grid,
  Input,
  InputAdornment,
  Link,
  Toolbar,
  alpha,
  useTheme,
} from "@mui/material";
import { Hanger as Logo, Magnify as SearchIcon } from "mdi-material-ui";

import NavigatorButtons from "./NavigatorButtons";
import { Link as RouterLink } from "react-router-dom";

const Navigator = () => {
  const theme = useTheme();

  const links = [
    {
      label: "Clothing",
      to: "/clothing",
    },
    {
      label: "Footwear",
      to: "/footwear",
    },
    {
      label: "Accessories",
      to: "/accessories",
    },
  ];

  return (
    <AppBar
      position="static"
      sx={{ backgroundColor: "#FFF", boxShadow: "none", marginBottom: 5 }}
    >
      <Toolbar disableGutters>
        <Grid container justifyContent="space-between" alignItems="center">
          <Grid
            container
            item
            xs={6}
            alignItems="center"
            justifyContent="space-between"
          >
            <Grid item xs={3}>
              <Box component={RouterLink} to="/">
                <Logo
                  sx={{
                    color: "#FFF",
                    backgroundColor: theme.palette.primary.main,
                    borderRadius: 1,
                  }}
                  fontSize="large"
                />
              </Box>
            </Grid>
            <Grid item container xs={9} spacing={5}>
              {links.map((link, index) => (
                <Grid item key={index}>
                  <Link
                    component={RouterLink}
                    to={link.to}
                    underline="none"
                    gutterBottom
                    sx={{
                      color: alpha("#000", 0.64),
                      fontSize: 18,
                      "&:hover": {
                        borderBottom: `2px solid ${alpha("#000", 0.64)}`,
                      },
                    }}
                  >
                    {link.label}
                  </Link>
                </Grid>
              ))}
            </Grid>
          </Grid>
          <Grid
            item
            container
            xs={6}
            justifyContent="flex-end"
            alignItems="center"
            spacing={3}
          >
            <Grid item xs={6}>
              <Input
                placeholder="Search for items and promotions"
                endAdornment={
                  <InputAdornment position="end">
                    <SearchIcon />
                  </InputAdornment>
                }
                sx={{ width: "80%" }}
              />
            </Grid>
            <NavigatorButtons />
          </Grid>
        </Grid>
      </Toolbar>
    </AppBar>
  );
};

export default Navigator;
