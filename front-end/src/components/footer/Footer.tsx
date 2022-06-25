import {
  Button,
  Grid,
  IconButton,
  InputAdornment,
  Link,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import {
  Facebook as FacebookIcon,
  Instagram as InstagramIcon,
  Pinterest as PinterestIcon,
  Twitter as TwitterIcon,
  Youtube as YoutubeIcon,
} from "mdi-material-ui";

import { ReactNode } from "react";
import { Link as RouterLink } from "react-router-dom";
import { grey } from "@mui/material/colors";

type GroupHeaderProps = {
  children: ReactNode;
};

const GroupHeader = (props: GroupHeaderProps) => {
  const { children } = props;

  const styles = {
    header: {
      color: "#FFF",
      fontSize: 18,
      marginBottom: 1,
    },
  };

  return <Typography sx={styles.header}>{children}</Typography>;
};

const Footer = () => {
  const columns = [
    {
      header: "ABOUT US",
      links: [
        {
          title: "Who we are",
          url: "",
        },
        {
          title: "Quality in the details",
          url: "",
        },
        {
          title: "Customer reviews",
          url: "",
        },
      ],
    },
    {
      header: "DEPARTMENTS",
      links: [
        {
          title: "Clothing",
          url: "",
        },
        {
          title: "Shoes",
          url: "",
        },
        {
          title: "Accessories",
          url: "",
        },
      ],
    },
    {
      header: "HELP",
      links: [
        {
          title: "Contact us",
          url: "",
        },
        {
          title: "Size guide",
          url: "",
        },
        {
          title: "Legal",
          url: "",
        },
      ],
    },
    {
      header: "PAYMENTS & DELIVERY",
      links: [
        {
          title: "Purchase terms",
          url: "",
        },
        {
          title: "Shipping",
          url: "",
        },
        {
          title: "Returns",
          url: "",
        },
      ],
    },
  ];

  const socialButtons = [
    {
      title: "Facebook",
      icon: <FacebookIcon />,
      url: "https://facebook.com",
    },
    {
      title: "Instagram",
      icon: <InstagramIcon />,
      url: "https://instagram.com",
    },
    {
      title: "Twitter",
      icon: <TwitterIcon />,
      url: "https://twitter.com",
    },
    {
      title: "YouTube",
      icon: <YoutubeIcon />,
      url: "https://youtube.com",
    },
    {
      title: "Pinterest",
      icon: <PinterestIcon />,
      url: "https://pinterest.com",
    },
  ];

  const styles = {
    footerContainer: {
      backgroundColor: "secondary.main",
      px: { xs: 8, lg: 32 },
      py: { xs: 4, lg: 16 },
      borderRadius: 0,
    },
    socialButton: {
      backgroundColor: "#F1F2F3",
      "&:hover": {
        backgroundColor: grey[400],
      },
      mr: 1,
      mb: 2,
    },
    subscribeField: {
      backgroundColor: "#FFF",
      borderRadius: 1,
      width: 400,
      minWidth: 400,
    },
    subscribeInput: {
      pr: 0,
    },
    linkContainer: {
      mb: 2,
    },
    link: {
      color: "#FFF",
      "&:hover": {
        color: "primary.main",
      },
    },
  };

  return (
    <Paper sx={styles.footerContainer}>
      <Grid container>
        {columns.map((column) => (
          <Grid
            item
            container
            direction="column"
            key={column.header}
            lg={3}
            md={3}
            sm={6}
            xs={12}
            sx={styles.linkContainer}
          >
            <GroupHeader>{column.header}</GroupHeader>
            {column.links.map((link) => (
              <Link
                key={link.url}
                component={RouterLink}
                to={link.url}
                underline="none"
                gutterBottom
              >
                <Typography sx={styles.link}>{link.title}</Typography>
              </Link>
            ))}
          </Grid>
        ))}
      </Grid>
      <Grid item container lg={12} sm={6} alignItems="flex-start">
        <Grid item xs={12}>
          <GroupHeader>SOCIAL</GroupHeader>
        </Grid>
        <Grid item container justifyContent="space-between">
          <Grid item>
            {socialButtons.map((button) => (
              <IconButton key={button.title} sx={styles.socialButton}>
                {button.icon}
              </IconButton>
            ))}
          </Grid>
          <Grid item>
            <TextField
              placeholder="Enter your email address"
              variant="outlined"
              sx={styles.subscribeField}
              size="small"
              InputProps={{
                sx: styles.subscribeInput,
                endAdornment: (
                  <InputAdornment position="end">
                    <Button variant="contained">SUBSCRIBE</Button>
                  </InputAdornment>
                ),
              }}
            />
          </Grid>
        </Grid>
      </Grid>
    </Paper>
  );
};

export default Footer;
