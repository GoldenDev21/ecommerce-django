import { Box, Button, GridProps, Stack, Typography } from "@mui/material";

interface Props extends GridProps {
  image: string;
  title: string;
  subtitle: string;
  buttonLabel?: string;
  description?: string;
  imagePosition?: string;
}

const ImageCard = (props: Props) => {
  const {
    image,
    title,
    subtitle,
    buttonLabel,
    description,
    imagePosition = "top-left",
  } = props;

  const styles = {
    container: {
      backgroundImage: `url(${image})`,
      backgroundPosition: imagePosition,
      backgroundSize: "cover",
      height: "100%",
      padding: 8,
    },
    description: {
      maxWidth: "50% !important",
    },
    button: {
      marginTop: 8,
      width: "50%",
    },
  };

  return (
    <Box sx={styles.container}>
      <Stack justifyContent="center" spacing={3}>
        <Typography variant="h6">{title}</Typography>
        <Typography variant="h3">{subtitle}</Typography>
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
