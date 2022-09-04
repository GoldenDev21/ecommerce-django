import { Color } from "../types/variant";

export const getSwatchColor = (color: Color) => {
  switch (color) {
    case Color.Black:
      return "black";
    case Color.Blue:
      return "blue";
    case Color.Beige:
      return "beige";
    case Color.Brown:
      return "brown";
    case Color.Gold:
      return "gold";
    case Color.Green:
      return "green";
    case Color.Grey:
      return "grey";
    case Color.Ivory:
      return "ivory";
    case Color.MultiColored:
      return "#FFF";
    case Color.Orange:
      return "orange";
    case Color.Pink:
      return "pink";
    case Color.Purple:
      return "purple";
    case Color.Red:
      return "red";
    case Color.Silver:
      return "silver";
    case Color.Turquoise:
      return "turquoise";
    case Color.White:
      return "white";
    case Color.Yellow:
      return "yellow";
    default:
      return "black";
  }
};
