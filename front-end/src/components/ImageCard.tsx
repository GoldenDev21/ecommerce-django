import { Button, Grid, GridProps, GridSize, Typography } from "@mui/material";

interface Props extends GridProps {
  image: string;
  title: string;
  subtitle: string;
  buttonLabel?: string;
  description?: string;
  gridWidth?: GridSize;
  imagePosition?: string;
}

const ImageCard = (props: Props) => {
  const {
    title,
    subtitle,
    description,
    image,
    buttonLabel,
    imagePosition = "top-left",
    ...gridProps
  } = props;

  const styles = {
    card: {
      padding: 8,
      backgroundImage: `url(${image})`,
      backgroundSize: "cover",
      backgroundPosition: imagePosition,
    },
    description: {
      maxWidth: "50% !important",
    },
  };

  return (
    <Grid
      item
      container
      direction="column"
      justifyContent="space-evenly"
      sx={styles.card}
      spacing={2}
      {...gridProps}
    >
      <Grid item>
        <Typography variant="h6">{title}</Typography>
      </Grid>
      <Grid item>
        <Typography variant="h3">{subtitle}</Typography>
      </Grid>
      {description && (
        <Grid item sx={styles.description}>
          <Typography>{description}</Typography>
        </Grid>
      )}
      {buttonLabel && (
        <Grid item>
          <Button
            variant="contained"
            size="large"
            disableElevation
            color="secondary"
          >
            {buttonLabel}
          </Button>
        </Grid>
      )}
    </Grid>
  );
};

export default ImageCard;
