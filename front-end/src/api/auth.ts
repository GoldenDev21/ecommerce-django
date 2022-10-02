import { Token, UserSignInRequestBody } from "../types/user";
import axios, { AxiosResponse } from "axios";

import apiName from "./api";

export const loginUser = (
  body: UserSignInRequestBody
): Promise<AxiosResponse<Token>> => {
  return axios.post(`${apiName}/auth/login/`, body);
};

export const logoutUser = (token: Token): Promise<AxiosResponse> => {
  const config = {
    headers: {
      Authorization: `Token ${token.token}`,
    },
  };
  return axios.post(`${apiName}/auth/logout/`, {}, config);
};
