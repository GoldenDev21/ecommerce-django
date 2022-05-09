import {Product, Season} from "./types/product"

import {Color} from "./types/variant"

export const mockProducts: Product[] = [
  {
    id: 12,
    name: 'Henriette Shoes',
    brand: 'CK',
    price: 29.99,
    season: Season.Spring,
    year: 2022,
    description: 'Lorem ipsum blahblahblah',
    category: '',
    url_key: '',
    variants: [
      {
        id: 6,
        sku: 'REW939R9MBLU',
        qty_in_stock: 122,
        color: Color.Blue,
        size: 'M',
        image: ''
      },
      {
        id: 7,
        sku: 'REW939R9SGRN',
        qty_in_stock: 111,
        color: Color.Green,
        size: 'S',
        image: ''
      },
    ]
  },
  {
    id: 13,
    name: 'Charlotte Sweater',
    brand: 'CK',
    price: 49.99,
    season: Season.Winter,
    year: 2022,
    description: 'Lorem ipsum blahblahblah',
    category: '',
    url_key: '',
    variants: [
      {
        id: 4,
        sku: 'REW939R9MBLU',
        qty_in_stock: 122,
        color: Color.Pink,
        size: 'M',
        image: ''
      },
      {
        id: 5,
        sku: 'REW939R9SGRN',
        qty_in_stock: 111,
        color: Color.Purple,
        size: 'S',
        image: ''
      },
    ]
  },
  {
    id: 14,
    name: 'Helia Hat',
    brand: 'CK',
    price: 29.99,
    season: Season.Summer,
    year: 2022,
    description: 'Lorem ipsum blahblahblah',
    category: '',
    url_key: '',
    variants: [
      {
        id: 2,
        sku: 'REW939R9MBLU',
        qty_in_stock: 122,
        color: Color.Beige,
        size: 'M',
        image: ''
      },
      {
        id: 3,
        sku: 'REW939R9SGRN',
        qty_in_stock: 111,
        color: Color.Red,
        size: 'S',
        image: ''
      },
    ]
  },
  {
    id: 16,
    name: 'Terra Shoes',
    brand: 'CK',
    price: 29.99,
    season: Season.Fall,
    year: 2022,
    description: 'Lorem ipsum blahblahblah',
    category: '',
    url_key: '',
    variants: [
      {
        id: 8,
        sku: 'REW939R9MBLU',
        qty_in_stock: 122,
        color: Color.Blue,
        size: 'M',
        image: ''
      },
      {
        id: 9,
        sku: 'REW939R9SGRN',
        qty_in_stock: 111,
        color: Color.Green,
        size: 'S',
        image: ''
      },
    ]
  },
  {
    id: 17,
    name: 'Bonnie Jeans',
    brand: 'CK',
    price: 29.99,
    season: Season.Spring,
    year: 2022,
    description: 'Lorem ipsum blahblahblah',
    category: '',
    url_key: '',
    variants: [
      {
        id: 10,
        sku: 'REW939R9MBLU',
        qty_in_stock: 122,
        color: Color.Blue,
        size: 'M',
        image: ''
      },
      {
        id: 11,
        sku: 'REW939R9SGRN',
        qty_in_stock: 111,
        color: Color.Green,
        size: 'S',
        image: ''
      },
    ]
  },
]