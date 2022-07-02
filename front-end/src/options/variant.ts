import { Size } from "../types/variant";

export const clothingSizes = [
  { label: "XS", value: Size.ExtraSmall },
  { label: "S", value: Size.Small },
  { label: "M", value: Size.Medium },
  { label: "L", value: Size.Large },
  { label: "XL", value: Size.ExtraLarge },
];

export const shoeSizes = Object.values(Size)
  .filter((value) => parseInt(value) && parseInt(value) !== 1)
  .map((value) => {
    return { label: value, value: value };
  });
