import { ImageList, ImageListItem, ImageListProps } from "@mui/material";

import { srcset } from "../utils/image";

interface Props extends Pick<ImageListProps, "cols" | "sx" | "rowHeight"> {
  imageData: { img: string; title: string; rows?: number; cols?: number }[];
  cols: number;
}

const ImageQuilt = (props: Props) => {
  const { imageData, cols, sx = {}, rowHeight = "auto" } = props;

  return (
    <ImageList variant="quilted" cols={cols} sx={sx} rowHeight={rowHeight}>
      {imageData.map((item) => (
        <ImageListItem
          key={item.img}
          cols={item.cols || 2}
          rows={item.rows || 1}
        >
          <img
            {...srcset(item.img, 300, item.rows)}
            alt={item.title}
            loading="lazy"
          />
        </ImageListItem>
      ))}
    </ImageList>
  );
};

export default ImageQuilt;
