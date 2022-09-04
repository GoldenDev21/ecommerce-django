import { Variant } from "./variant";
import { Category } from "./category";

export interface Product {
  active: boolean;
  brand: string;
  category: Category;
  department: Department;
  description: string;
  id: number;
  in_stock: boolean;
  name: string;
  price: number;
  season: Season;
  url_key: string;
  variants: Variant[];
  year: number;
}

export enum Season {
  Winter = 1,
  Spring = 2,
  Summer = 3,
  Fall = 4,
}

export enum Department {
  Clothing = 1,
  Shoes = 2,
  Accessories = 3,
}
