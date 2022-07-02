import { Typography, TypographyProps } from "@mui/material";

type Props = {
  children: TypographyProps["children"];
};

const FilterLabel = ({ children }: Props) => {
  return <Typography variant="h6">{children}</Typography>;
};

export default FilterLabel;
