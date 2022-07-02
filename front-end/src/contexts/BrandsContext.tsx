import { ReactNode, createContext, useEffect, useState } from "react";

import { Brand } from "../types/brand";
import { getBrands } from "../api/brand";

type Props = {
  children: ReactNode;
};

export const BrandsContext = createContext<{ brands: Brand[] }>({ brands: [] });

export const BrandsProvider = (props: Props) => {
  const { children } = props;

  const [brands, setBrands] = useState<Brand[]>([]);

  useEffect(() => {
    getBrands()
      .then((response) => {
        setBrands(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <BrandsContext.Provider value={{ brands }}>
      {children}
    </BrandsContext.Provider>
  );
};
