import {
  AccountOutline as AccountIcon,
  CartOutline as CartIcon,
  HeartOutline as FavoritesIcon,
} from "mdi-material-ui";
import { Grid, IconButton, Menu, MenuItem } from "@mui/material";
import { MouseEvent, useState } from "react";

const NavigatorButtons = () => {
  const [anchorEl, setAnchorEl] = useState<HTMLElement | null>(null);
  const open = Boolean(anchorEl);

  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <>
      <Grid item>
        <IconButton onClick={handleClick}>
          <AccountIcon />
        </IconButton>
      </Grid>
      <Grid item>
        <IconButton>
          <FavoritesIcon />
        </IconButton>
      </Grid>
      <Grid item>
        <IconButton>
          <CartIcon />
        </IconButton>
      </Grid>
      <Menu anchorEl={anchorEl} open={open} onClose={handleClose}>
        <MenuItem onClick={handleClose}>Profile</MenuItem>
        <MenuItem onClick={handleClose}>My account</MenuItem>
        <MenuItem onClick={handleClose}>Logout</MenuItem>
      </Menu>
    </>
  );
};

export default NavigatorButtons;
