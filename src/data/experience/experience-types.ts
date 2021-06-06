import { DateTime } from "luxon"
import { DataProvider, State } from "../common/common-types"

export const EMPLOYMENTS = ['Full Time', 'Part Time'] as const
export type Employment = typeof EMPLOYMENTS[number]

export interface Experience {
  position: string
  employer: string
  employment: Employment
  startDate: DateTime,
  endDate: DateTime,
  tags: string[]
}

export interface ExperienceJSON {
  position: string
  employer: string
  employment: string
  start_date: string
  end_date: string
  tags: string[]
}

export type ExperienceState = State<Experience[]>

export type ExperienceDataProvider = DataProvider<ExperienceJSON[]>