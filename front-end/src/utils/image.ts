export const srcset = (image: string, size: number, rows = 1) => {
  return {
    src: `${image}?w=${size * 2}&h=${size * rows}&fit=crop&auto=format`,
    srcSet: `${image}?w=${size * 2}&h=${
      size * rows
    }&fit=crop&auto=format&dpr=2 2x`,
  };
}