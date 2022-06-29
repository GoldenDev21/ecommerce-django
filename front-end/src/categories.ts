import {Category} from "./types/category"

export const categories = [
  {
    label: "Clothing",
    subCategories: [
      {
        label: "Dresses",
        to: "/dresses",
        category: Category.Dresses
      },
      {
        label: "Jeans",
        to: "/jeans",
        category: Category.Jeans
      },
      {
        label: "Pants",
        to: "/pants",
        category: Category.Pants
      },
      {
        label: "Jackets",
        to: "/jackets",
        category: Category.Jackets
      },
      {
        label: "Skirts",
        to: "/skirts",
        category: Category.Skirts
      },
      {
        label: "Blouses",
        to: "/blouses",
        category: Category.Blouses
      },
      {
        label: "T-Shirts",
        to: "/t-shirts",
        category: Category.TShirts
      },
      {
        label: "Outerwear",
        to: "/outerwear",
        category: Category.Outerwear
      },
      {
        label: "Sets",
        to: "/sets",
        category: Category.Sets
      },
      {
        label: "Sweaters",
        to: "/sweaters",
        category: Category.Sweaters
      }, 
      {
        label: "Sportswear",
        to: "/sportswear",
        category: Category.Sportswear
      },
      {
        label: "Sleepwear",
        to: "/sleepwear",
        category: Category.Sleepwear
      },
    ],
  },
  {
    label: "Footwear",
    subCategories: [
      {
        label: "Sandals",
        to: "/sandals",
        category: Category.Sandals
      },
      {
        label: "Heels",
        to: "/heels",
        category:Category.Heels
      },
      {
        label: "Sneakers",
        to: "/sneakers",
        category:Category.Sneakers
      },
      {
        label: "Boots",
        to: "/boots",
        category:Category.Boots
      },
      {
        label: "Ballet Flats",
        to: "/ballet-flats",
        category:Category.BalletFlats
      },
      {
        label: "Loafers",
        to: "/loafers",
        category:Category.Loafers
      },
    ],
  },
  {
    label: "Accessories",
    subCategories: [
      {
        label: "Bags",
        to: "/bags",
        category:Category.Bags
      },
      {
        label: "Sunglasses",
        to: "/sunglasses",
        category:Category.Sunglasses
      },
      {
        label: "Jewelry",
        to: "/jewelry",
        category:Category.Jewelry
      },
      {
        label: "Wallets",
        to: "/wallets",
        category:Category.Wallets
      },
      {
        label: "Belts",
        to: "/belts",
        category: Category.Belts
      },
      {
        label: "Hats",
        to: "/hats",
        category: Category.Hats
      },
      {
        label: "Scarves",
        to: "/scarves",
        category: Category.Scarves
      },
    ],
  },
];