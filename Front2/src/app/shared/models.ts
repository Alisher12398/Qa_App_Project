export interface IUser {
  id: number,
  username: string,
  email: string
}

export interface IGroup {
  id: number,
  title: string,
  image_name: string,
  price: number
}

export interface IQa {
  id: number,
  question: string,
  answer_1: string,
  answer_2: string,
  answer_3: string,
  answer_4: string,
  answer_right: number
}

export interface IAuthResponse {
  token: string;
}

export interface IContactNew {
  id: number,
  name: string,
  phone: string,
  owner: IUser
}
