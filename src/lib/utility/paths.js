export const cloudPrefix = 'https://jbphd-pub.s3.us-west-000.backblazeb2.com'

export const noext = (str) => {
    return str.slice(0, -4).replace('+', '%2B')
}