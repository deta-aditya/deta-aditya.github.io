import { DateTime } from "luxon"
import { Employment, EMPLOYMENTS, Experience, ExperienceJSON } from "./experience-types"

export function fromJSON(json: ExperienceJSON): Experience {
  let experience: Partial<Experience> = {
    position: json.position,
    employer: json.employer,
    tags: json.tags,
  }

  experience.startDate = DateTime.fromISO(json.start_date)
  experience.endDate = DateTime.fromISO(json.end_date)

  try {
    experience.employment = parseEmployment(json.employment)
  } catch (e) {
    throw new Error(`Incorrect ExperienceJSON data. ${e.message}`)
  }

  return experience as Experience
}

export function parseEmployment(employmentString: string): Employment {
  const maybeValidName = EMPLOYMENTS.find(validName => validName === employmentString)

  if (maybeValidName !== undefined) {
    return maybeValidName
  }

  throw new Error(`Invalid Employment type: ${employmentString}.`)
}