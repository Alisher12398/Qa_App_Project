export interface IUser {
  id: number,
  username: string,
  email: string
}

export interface IProfile{
  id: number,
  username: string,
  user_points: number,
  avatar: string
}

export interface ICompany {
  id: number,
  name: string,
}

export interface IOffers {
  id: number,
  id_company: string,
  title: string
}

export interface IOffersPurchases {
  id: number,
  owner: string,
  id_offer: string,
  promocode: string,
  purchase_day: string
}

export interface IQa {
  id: number,
  id_group: number,
  question: string,
  answer_1: string,
  answer_2: string,
  answer_3: string,
  answer_4: string,
  answer_right: number
}
