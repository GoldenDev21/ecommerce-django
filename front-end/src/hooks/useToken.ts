import { Token } from "../types/user";
import { useEffect } from "react";

export default function useToken() {
  const getToken = (): Token | null => {
    const storedToken = localStorage.getItem("token");
    return storedToken ? JSON.parse(storedToken) : null;
  };

  const saveToken = (token: Token) => {
    localStorage.setItem("token", JSON.stringify(token));
  };

  const removeToken = () => {
    localStorage.removeItem("token");
  };

  const tokenIsExpired = (date: string) => {
    const dateObj = new Date(date);
    if (dateObj < new Date()) {
      return true;
    }
    return false;
  };

  const token = getToken();

  useEffect(() => {
    if (token && tokenIsExpired(token.expiry)) {
      removeToken();
    }
  }, [token]);

  return {
    saveToken,
    getToken,
    removeToken,
  };
}
