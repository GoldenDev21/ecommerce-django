import {
  AccountOutline as AccountIcon,
  CartOutline as CartIcon,
  HeartOutline as FavoritesIcon,
} from "mdi-material-ui";
import { Grid, IconButton, Menu, MenuItem } from "@mui/material";
import { MouseEvent, useContext, useState } from "react";

import { UserContext } from "../../contexts/UserContext";
import { useNavigate } from "react-router-dom";

const NavigatorButtons = () => {
  const [anchorEl, setAnchorEl] = useState<HTMLElement | null>(null);
  const open = Boolean(anchorEl);

  const { isUserSignedIn, handleLogoutUser } = useContext(UserContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    handleLogoutUser();
    navigate("/");
  };

  const handleClick = (event: MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const getProfileMenuItems = () => {
    if (isUserSignedIn) {
      return [
        {
          label: "Profile",
          onClick: () => {},
        },
        {
          label: "My account",
          onClick: () => {},
        },
        {
          label: "Logout",
          onClick: handleLogout,
        },
      ];
    } else {
      return [
        {
          label: "Login",
          onClick: () => navigate("/login"),
        },
        {
          label: "Sign up",
          onClick: () => {},
        },
      ];
    }
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
        {getProfileMenuItems().map(({ label, onClick }) => (
          <MenuItem onClick={onClick} key={label}>
            {label}
          </MenuItem>
        ))}
      </Menu>
    </>
  );
};

export default NavigatorButtons;
