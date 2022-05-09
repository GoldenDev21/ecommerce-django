import {Color} from "../types/variant"

export const getSwatchColor = (color: Color) => {

  const colorKeys = Object.keys(Color).map(color => color.toLowerCase());

  console.log(colorKeys, color)

  switch(color){
    case Color.Black:
      return "black"
    case Color.Blue:
      return "blue"
    case Color.Beige:
      return "beige"
    case Color.Brown:
      return "brown"
    case Color.Gold:
      return "gold"
    case Color.Green:
      return "green"
    case Color.Grey:
      return "grey"
    case Color.Ivory:
      return "ivory"
    case Color.MultiColored:
      return "#FFF"
    case Color.Orange:
      return "#FFF"
    case Color.Pink:
      return "#FFF"
    case Color.Purple:
      return "#FFF"
    case Color.Red:
      return "#FFF"
    case Color.Silver:
      return "#FFF"
    case Color.Turquoise:
      return "#FFF"
    case Color.White:
      return "#FFF"
    case Color.Yellow:
      return "#FFF"
    default:
      return '#FFF'
  }
}