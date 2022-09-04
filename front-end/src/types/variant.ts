export type Variant = {
  color: Color;
  id: number;
  image: string;
  qty_in_stock: number;
  size: Size;
  sku: string;
};

export enum Color {
  Black = "BLK",
  Blue = "BLU",
  Beige = "BEI",
  Brown = "BRN",
  Gold = "GLD",
  Green = "GRN",
  Grey = "GRY",
  Ivory = "IVR",
  MultiColored = "MLT",
  Orange = "ORN",
  Pink = "PNK",
  Purple = "PRP",
  Red = "RED",
  Silver = "SLV",
  Turquoise = "TRQ",
  White = "WHT",
  Yellow = "YLL",
}

export enum Size {
  ExtraSmall = "XS",
  Small = "S",
  Medium = "M",
  Large = "L",
  ExtraLarge = "XL",
  OneSize = "1",
  ThirtyTwo = "32",
  ThirtyFour = "34",
  ThirtySix = "36",
  ThirtySeven = "37",
  ThirtyEight = "38",
  ThirtyNine = "39",
  Forty = "40",
  FortyOne = "41",
  FortyTwo = "42",
}
