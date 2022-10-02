import { Token, User } from "../types/user";
import axios, { AxiosResponse } from "axios";

import apiName from "./api";

export const getCurrentUser = (token: Token): Promise<AxiosResponse<User>> => {
  const config = {
    headers: {
      Authorization: `Token ${token.token}`,
    },
  };
  return axios.get(`${apiName}/users/current`, config);
};
