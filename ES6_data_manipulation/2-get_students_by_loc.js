export default function getStudentsByLocation(data, city) {
  return data.filter((data) => data.location === city);
}
