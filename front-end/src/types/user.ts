export type User = {
  date_joined: string;
  email: string;
  first_name: string;
  id: number;
  is_active: boolean;
  is_on_mailing_list: boolean;
  is_staff: boolean;
  is_superuser: boolean;
  last_login: string;
  last_name: string;
};

export type Token = {
  expiry: string;
  token: string;
};

export type UserSignInRequestBody = {
  username: string;
  password: string;
};
