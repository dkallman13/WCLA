import Image from 'next/image'
import styles from './page.module.css'
import Head from './header'

export default function Home() {
  return (
    <div className={styles.main}>
      <Head></Head>
      <h2>welcome to my personal log webiste!</h2>
    </div>
  )
}
