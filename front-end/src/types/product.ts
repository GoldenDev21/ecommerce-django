import { Variant } from "./variant";

export interface Product {
  id: number;
  brand: string;
  category: string;
  description: string;
  name: string;
  price: number;
  season: Season;
  url_key: string;
  variants: Variant[]
  year: number;
}

export enum Season {
  Winter = 1,
  Spring = 2,
  Summer = 3,
  Fall = 4
}