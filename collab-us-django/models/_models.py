
"""
__Seed builder__v0.1.8
  AUTO_GENERATED (Use seed-builder to modify)

- Business
   -  id: int
   -  name: string
   -  address_cords: string
   -  contact_1: string
   -  contact_2: string
   -  contact_3: string
   -  contact_4: string
   -  tags: text
   -  is_local: boolean
   -  opening_time: date
   -  closing_time: date
   -  open_days: string
   -  verified: boolean
   -  user: user
   -  category: category

- Category
   -  id: int
   -  name: enum

- Stat
   -  id: int
   -  prop_1: int
   -  prop_2: int
   -  prop_3: int
   -  prop_4: int
   -  comment: string
   -  business: business[]
   -  user: user

- User
   -  id: int
   -  username: string
   -  first_name: string
   -  last_name: string
   -  email: string
   -  is_active: boolean
   -  user_type: user_type

- UserType
   -  id: int
   -  name: enum
"""

