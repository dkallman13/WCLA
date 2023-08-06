import Image from 'next/image'
import styles from './page.module.css'
import Head from './header'

export default function Home() {
  return (
    <main className={styles.main}>
      <Head></Head>
    </main>
  )
}
