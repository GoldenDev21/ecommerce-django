import {
  AppBar,
  Box,
  Grid,
  IconButton,
  Input,
  InputAdornment,
  Link,
  MenuItem,
  Paper,
  Popper,
  Toolbar,
  Typography,
  alpha,
  useTheme,
} from "@mui/material";
import { Hanger as Logo, Magnify as SearchIcon } from "mdi-material-ui";

import MenuIcon from "@mui/icons-material/Menu";
import NavigatorButtons from "./NavigatorButtons";
import { Link as RouterLink } from "react-router-dom";
import { useState } from "react";

const Navigator = () => {
  const theme = useTheme();
  const { breakpoints, palette } = theme;

  const [anchorEl, setAnchorEl] = useState<HTMLElement | null>(null);

  const handleOpenMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorEl(null);
  };

  const getSubCategories = (menuId: string) => {
    const foundLink = categories.find(
      (category) => category.label.toLowerCase() === menuId
    );
    return foundLink
      ? foundLink.subCategories.sort((a, b) => (a.label > b.label ? 1 : -1))
      : [];
  };

  const getElementId = (element: HTMLElement) => {
    return element.getAttribute("id");
  };

  const categories = [
    {
      label: "Clothing",
      subCategories: [
        {
          label: "Dresses",
          to: "/dresses",
        },
        {
          label: "Jeans",
          to: "/jeans",
        },
        {
          label: "Pants",
          to: "/pants",
        },
        {
          label: "Jackets",
          to: "/jackets",
        },
        {
          label: "Skirts",
          to: "/skirts",
        },
        {
          label: "Blouses",
          to: "/blouses",
        },
        {
          label: "T-Shirts",
          to: "/t-shirts",
        },
        {
          label: "Outerwear",
          to: "/outerwear",
        },
        {
          label: "Sets",
          to: "/sets",
        },
        {
          label: "Sweaters",
          to: "/sweaters",
        },
        {
          label: "Sportswear",
          to: "/sportswear",
        },
        {
          label: "Sleepwear",
          to: "/sleepwear",
        },
      ],
    },
    {
      label: "Footwear",
      subCategories: [
        {
          label: "Sandals",
          to: "/sandals",
        },
        {
          label: "Heels",
          to: "/heels",
        },
        {
          label: "Sneakers",
          to: "/sneakers",
        },
        {
          label: "Boots",
          to: "/boots",
        },
        {
          label: "Ballet Flats",
          to: "/ballet-flats",
        },
        {
          label: "Loafers",
          to: "/loafers",
        },
      ],
    },
    {
      label: "Accessories",
      subCategories: [
        {
          label: "Bags",
          to: "/bags",
        },
        {
          label: "Sunglasses",
          to: "/sunglasses",
        },
        {
          label: "Jewelry",
          to: "/jewelry",
        },
        {
          label: "Wallets",
          to: "/wallets",
        },
        {
          label: "Belts",
          to: "/belts",
        },
        {
          label: "Hats",
          to: "/hats",
        },
        {
          label: "Scarves",
          to: "/scarves",
        },
      ],
    },
  ];

  const darkBorder = `2px solid ${alpha("#000", 0.64)}`;
  const styles = {
    appBar: {
      backgroundColor: "#FFF",
      boxShadow: "none",
      marginBottom: 5,
    },
    category: {
      borderBottom: `2px solid #FFF`,
      [breakpoints.down("lg")]: {
        fontSize: 16,
      },
      color: alpha("#000", 0.64),
      cursor: "default",
      fontSize: 18,
      "&:hover": {
        borderBottom: darkBorder,
      },
    },
    categoryHover: {
      borderBottom: darkBorder,
    },
    hideOnLargeScreens: {
      [breakpoints.up("md")]: {
        display: "none",
      },
    },
    hideOnSmallScreens: {
      [breakpoints.down("md")]: {
        display: "none",
      },
    },
    logo: {
      backgroundColor: palette.primary.main,
      borderRadius: 1,
      color: "#FFF",
    },
    menuContainer: {
      marginTop: -4,
      padding: 5,
    },
    menu: {
      padding: 0,
    },
    searchBox: {
      width: "80%",
    },
  };

  const showUnderline = (label: string) =>
    anchorEl && getElementId(anchorEl) === label.toLowerCase();

  return (
    <>
      <AppBar position="static" sx={styles.appBar}>
        <Toolbar disableGutters>
          <Grid container justifyContent="space-between" alignItems="center">
            <Grid
              container
              item
              xs={6}
              alignItems="center"
              justifyContent="space-between"
            >
              <Grid item xs={3} sx={styles.hideOnSmallScreens}>
                <Box component={RouterLink} to="/">
                  <Logo sx={styles.logo} fontSize="large" />
                </Box>
              </Grid>
              <Grid item xs={3} sx={styles.hideOnLargeScreens}>
                <IconButton>
                  <MenuIcon color="primary" fontSize="medium" />
                </IconButton>
              </Grid>
              <Grid
                item
                container
                xs={9}
                spacing={5}
                sx={styles.hideOnSmallScreens}
              >
                {categories.map((category) => (
                  <Grid item key={category.label}>
                    <Typography
                      id={category.label.toLowerCase()}
                      gutterBottom
                      sx={[
                        styles.category,
                        showUnderline(category.label) && styles.categoryHover,
                      ]}
                      onMouseEnter={handleOpenMenu}
                    >
                      {category.label}
                    </Typography>
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
              sx={styles.hideOnSmallScreens}
            >
              <Grid item xs={6}>
                <Input
                  placeholder="Search for items and promotions"
                  endAdornment={
                    <InputAdornment position="end">
                      <SearchIcon />
                    </InputAdornment>
                  }
                  sx={styles.searchBox}
                />
              </Grid>
              <NavigatorButtons />
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
      <Popper
        open={Boolean(anchorEl)}
        anchorEl={anchorEl}
        placement="bottom"
        onMouseLeave={handleCloseMenu}
      >
        <Box sx={styles.menuContainer}>
          <Paper sx={styles.menu}>
            {getSubCategories(anchorEl?.id ?? "").map((subCategory) => (
              <MenuItem key={subCategory.label}>
                <Typography>
                  <Link
                    component={RouterLink}
                    to={subCategory.to}
                    underline="none"
                    gutterBottom
                    color="secondary"
                  >
                    {subCategory.label}
                  </Link>
                </Typography>
              </MenuItem>
            ))}
          </Paper>
        </Box>
      </Popper>
    </>
  );
};

export default Navigator;
