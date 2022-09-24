import axios, { AxiosResponse } from "axios";

import apiName from "./api";

export const authenticateUser = (body: any): Promise<AxiosResponse<any>> => {
  return axios.post(`${apiName}/auth/login/`, body);
};
