export interface Variant {
  color: string;
  id: number;
  image: string;
  qty_in_stock: number;
  size: string;
  sku: string;
}

export enum Color {
  Black = 'BLK',
  Blue = 'BLU',
  Beige = 'BEI',
  Brown = 'BRN',
  Gold = 'GLD',
  Green = 'GRN',
  Grey = 'GRY',
  Ivory = 'IVR',
  MultiColored = 'MLT',
  Orange = 'ORN',
  Pink = 'PNK',
  Purple = 'PRP',
  Red = 'RED',
  Silver = 'SLV',
  Turquoise = 'TRQ',
  White = 'WHT',
  Yellow = 'YLL'
}