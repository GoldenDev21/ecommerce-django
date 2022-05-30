import {
  Box,
  Collapse,
  Drawer,
  DrawerProps,
  List,
  ListItemButton,
  ListItemText,
} from "@mui/material";
import { ExpandLess, ExpandMore } from "@mui/icons-material";
import { Fragment, MouseEvent, useState } from "react";

import { Link as RouterLink } from "react-router-dom";
import { categories as baseCategories } from "../../categories";

type Props = {
  open: DrawerProps["open"];
  onClose: () => void;
};

const NavigatorDrawer = (props: Props) => {
  const { open, onClose } = props;

  const extraCategories = [
    {
      label: "My Account",
      subCategories: [
        {
          label: "Profile",
          to: "/profile",
        },
        {
          label: "Favorites",
          to: "/favorites",
        },
        {
          label: "Logout",
          to: "/logout",
        },
      ],
    },
    {
      label: "Help",
      subCategories: [
        {
          label: "Size guide",
          to: "",
        },
        {
          label: "Contact us",
          to: "/contact",
        },
        {
          label: "FAQ",
          to: "/faq",
        },
      ],
    },
  ];

  const categories = [...baseCategories, ...extraCategories];

  const [selectedSubmenu, setSelectedSubmenu] = useState<HTMLElement | null>(
    null
  );

  const handleToggleSubmenu = (event: MouseEvent<HTMLElement>) => {
    const currentId = event.currentTarget.getAttribute("id");
    if (currentId && isSubmenuOpen(currentId)) {
      setSelectedSubmenu(null);
    } else {
      setSelectedSubmenu(event.currentTarget);
    }
  };

  const isSubmenuOpen = (id: string) => {
    if (!selectedSubmenu) {
      return false;
    }
    return id === selectedSubmenu.getAttribute("id");
  };

  const styles = {
    drawer: {
      width: "66vw",
    },
    listButton: {
      paddingLeft: 4,
    },
  };

  return (
    <Box>
      <Drawer open={open} onClose={onClose}>
        <List sx={styles.drawer}>
          {categories.map((category) => {
            const id = category.label.toLowerCase();
            const isOpen = isSubmenuOpen(id);
            return (
              <Fragment key={category.label}>
                <ListItemButton onClick={handleToggleSubmenu} id={id}>
                  <ListItemText
                    primary={category.label}
                    primaryTypographyProps={{
                      fontSize: 18,
                    }}
                  />
                  {isOpen ? <ExpandLess /> : <ExpandMore />}
                </ListItemButton>
                <Collapse in={isOpen} timeout="auto" unmountOnExit>
                  <List disablePadding>
                    {category.subCategories
                      .sort((a, b) => (a.label > b.label ? 1 : -1))
                      .map((subCategory) => (
                        <ListItemButton
                          sx={styles.listButton}
                          key={subCategory.label}
                          component={RouterLink}
                          to={subCategory.to}
                        >
                          {subCategory.label}
                        </ListItemButton>
                      ))}
                  </List>
                </Collapse>
              </Fragment>
            );
          })}
        </List>
      </Drawer>
    </Box>
  );
};

export default NavigatorDrawer;
