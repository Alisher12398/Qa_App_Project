export interface IUser {
  id: number,
  username: string,
  email: string
}

export interface ICompany {
  id: number,
  name: string
}

export interface IProfile{
  id: number,
  username: string,
  user_points: number,
  avatar: string
}

export interface IOffers {
  id: number,
  id_company: ICompany,
  title: string
}

export interface IOffersPurchases {
  id: number,
  owner: string,
  id_offer: IOffers,
  promocode: string,
  purchase_day: string
}

