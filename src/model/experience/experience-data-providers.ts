import { ExperienceDataProvider, ExperienceJSON } from "./experience-types"
import experiences from '../../data/experience.json'

export const getFromLocalJSON: ExperienceDataProvider = () => {
  return Promise.resolve(experiences as ExperienceJSON[])
}