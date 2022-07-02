import axios, {AxiosResponse} from "axios";

import {Brand} from "../types/brand"
import apiName from "./api"

export const getBrands = (): Promise<AxiosResponse<Brand[]>> => {
  return axios.get(`${apiName}/brands/`)
}