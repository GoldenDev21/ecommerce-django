import axios, { AxiosResponse } from "axios";

import { Product } from "../types/product";
import apiName from "./api";

export const getProducts = (params: any): Promise<AxiosResponse<Product[]>> => {
  return axios.get(`${apiName}/products/`, { params: params });
};
