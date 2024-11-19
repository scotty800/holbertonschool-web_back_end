export default function getStudentIdsSum(data) {
  return data.reduce((sum, data) => sum + data.id, 0);
}
