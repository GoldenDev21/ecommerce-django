import { Box, Button, GridProps, Stack, Typography } from "@mui/material";

import { srcset } from "../utils/image";

interface Props extends GridProps {
  image: string;
  imageAlt: string;
  title: string;
  subtitle: string;
  buttonLabel?: string;
  description?: string;
  textContainerSx?: { [key: string]: string | number };
  imageSx?: { [key: string]: string | number };
}

const ImageCard = (props: Props) => {
  const {
    image,
    title,
    subtitle,
    buttonLabel,
    description,
    imageAlt,
    textContainerSx = {
      left: "10%",
      top: "30%",
    },
    imageSx = {},
  } = props;

  const styles = {
    container: {
      height: "100%",
    },
    description: {
      maxWidth: "50% !important",
    },
    button: {
      marginTop: 8,
      width: "50%",
    },
    textContainer: {
      position: "absolute",
      ...textContainerSx,
    },
    image: {
      ...imageSx,
    },
    text: {
      textAlign: "start",
    },
  };

  return (
    <Box sx={styles.container}>
      <Box
        component="img"
        {...srcset(image, 500)}
        alt={imageAlt}
        sx={styles.image}
      />
      <Stack spacing={3} sx={styles.textContainer}>
        <Typography variant="h6" sx={styles.text}>
          {title}
        </Typography>
        <Typography variant="h3" sx={styles.text}>
          {subtitle}
        </Typography>
        {description && (
          <Typography sx={styles.description}>{description}</Typography>
        )}
        {buttonLabel && (
          <Button
            variant="contained"
            size="large"
            disableElevation
            color="secondary"
            sx={styles.button}
          >
            {buttonLabel}
          </Button>
        )}
      </Stack>
    </Box>
  );
};

export default ImageCard;
