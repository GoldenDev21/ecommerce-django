import { ReactNode, createContext, useEffect, useState } from "react";
import { Token, User, UserSignInRequestBody } from "../types/user";
import { loginUser, logoutUser } from "../api/auth";

import { getCurrentUser } from "../api/user";

type Props = {
  children: ReactNode;
};

type UserContextType = {
  handleLoginUser: (body: UserSignInRequestBody) => void;
  handleLogoutUser: () => void;
  isUserSignedIn: boolean;
  user: User | null;
};

export const UserContext = createContext<UserContextType>({
  handleLoginUser: () => {},
  handleLogoutUser: () => {},
  isUserSignedIn: false,
  user: null,
});

export const UserProvider = ({ children }: Props) => {
  const [user, setUser] = useState<User | null>(null);
  const [isFetching, setIsFetching] = useState(true);
  const [token, setToken] = useState<Token | null>(null);

  const getToken = () => {
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      setToken(JSON.parse(storedToken));
    }
  };

  const saveToken = (token: Token) => {
    localStorage.setItem("token", JSON.stringify(token));
    setToken(token);
  };

  const removeToken = () => {
    localStorage.removeItem("token");
    setToken(null);
  };

  const tokenIsExpired = (expiry: string) => {
    const expirationDate = new Date(expiry);
    const today = new Date();
    if (expirationDate < today) {
      return true;
    }
    return false;
  };

  useEffect(() => {
    if (token && tokenIsExpired(token.expiry)) {
      removeToken();
    }
  }, [token]);

  useEffect(() => {
    getToken();
  }, []);

  const fetchUser = async (token: Token) => {
    setIsFetching(true);

    try {
      const { data } = await getCurrentUser(token);
      setUser(data);
    } catch (error) {
      console.error(error);
    } finally {
      setIsFetching(false);
    }
  };

  const isUserSignedIn = Boolean(user && !isFetching);

  useEffect(() => {
    if (!token) {
      return;
    }
    fetchUser(token);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  const handleLogoutUser = async () => {
    if (token) {
      try {
        await logoutUser(token);
        setUser(null);
        removeToken();
      } catch (e) {
        console.error(e);
      }
    }
  };

  const handleLoginUser = async (body: UserSignInRequestBody) => {
    try {
      const { data } = await loginUser(body);
      saveToken(data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <UserContext.Provider
      value={{ handleLoginUser, handleLogoutUser, isUserSignedIn, user }}
    >
      {children}
    </UserContext.Provider>
  );
};
