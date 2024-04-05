<template>
    <div class="hero-section-inner">
      <div class="highlighted-parent">
        <div class="highlighted">
          <div class="frame-parent2">
            <div class="great-sound-with-solo-headphon-parent">
              <h1 class="great-sound-with-container">
                <p class="great-sound">Great Sound</p>
                <p class="with-solo">With Solo</p>
                <p class="headphone">Headphone</p>
              </h1>
              <div class="you-made-it">
                It is a long established fact that a reader will be distracted by
                the readable content of a page when looking at its layout. The
                point of using Lorem Ipsum.
              </div>
            </div>
            <button class="button8">
              <div class="button9">Shop Now</div>
              <div class="tag-input">
                <img class="huge-iconarrowssolidarrow-r" alt="" />
              </div>
            </button>
          </div>
        </div>
        <div class="disconnected-parent">
          <div class="disconnected" />
          <img
            class="young-handsome-happy-smiling-m-icon"
            loading="lazy"
            alt=""
            src="/younghandsomehappysmilingmandancinglisteningmusicheadphonesisolatedwhitestudiowall-1@2x.png"
          />
        </div>
      </div>
    </div>
</template>

<script>
    import { defineComponent } from "vue";
  
    export default defineComponent({
      name: "HomePage",
    });
</script>

<style scoped>
    .great-sound {
      margin: 0;
    }
    .with-solo {
      margin: 0;
    }
    .headphone {
      margin: 0;
    }
    .great-sound-with-container {
      margin: 0;
      align-self: stretch;
      position: relative;
      font-size: inherit;
      line-height: 110px;
      font-weight: 700;
      font-family: inherit;
      z-index: 2;
    }
    .you-made-it {
      width: 514px;
      position: relative;
      font-size: var(--header-7-bold-size);
      line-height: 30px;
      display: inline-block;
      max-width: 100%;
      z-index: 2;
    }
    .great-sound-with-solo-headphon-parent {
      align-self: stretch;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      max-width: 100%;
    }
    .button9 {
      position: relative;
      font-size: var(--body-1-regular-size);
      line-height: 30px;
      font-family: var(--body-1-regular);
      color: var(--white-500);
      text-align: left;
      display: inline-block;
      min-width: 83px;
    }
    .huge-iconarrowssolidarrow-r {
      width: 24px;
      height: 24px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .tag-input {
      height: 27px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-10xs) 0px 0px;
      box-sizing: border-box;
    }
    .button8 {
      cursor: pointer;
      border: none;
      padding: var(--padding-smi) var(--padding-xl);
      background-color: var(--primary-500);
      border-radius: var(--br-3xs);
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-3xs);
      z-index: 2;
    }
    .frame-parent2 {
      align-self: stretch;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      gap: var(--gap-19xl);
      flex-shrink: 0;
    }
    .highlighted {
      width: 544px;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: flex-start;
      padding: var(--padding-121xl) 0px 0px;
      box-sizing: border-box;
      min-width: 544px;
      max-width: 100%;
    }
    .disconnected {
      position: absolute;
      top: 73px;
      left: -11px;
      border-radius: 50%;
      background-color: var(--white-500);
      width: 658px;
      height: 658px;
      z-index: 2;
    }
    .young-handsome-happy-smiling-m-icon {
      position: absolute;
      height: 100%;
      top: 0px;
      bottom: 0px;
      left: 26px;
      max-height: 100%;
      width: 599px;
      object-fit: cover;
      z-index: 3;
    }
    .disconnected-parent {
      height: 814px;
      flex: 1;
      position: relative;
      min-width: 421px;
      flex-shrink: 0;
    }
    .highlighted-parent {
      width: 1191px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: center;
      max-width: 100%;
      row-gap: 20px;
    }
    .hero-section-inner {
      width: 1389px;
      display: flex;
      flex-direction: row;
      align-items: flex-start;
      justify-content: center;
      padding: 0px var(--padding-xl);
      box-sizing: border-box;
      max-width: 100%;
      text-align: left;
      font-size: var(--header-1-bold-size);
      color: var(--dark-500);
      font-family: var(--body-1-regular);
    }
  
    @media screen and (max-width: 1050px) {
      .great-sound-with-container {
        font-size: var(--header-3-bold-size);
        line-height: 66px;
      }
  
      .highlighted {
        flex: 1;
      }
  
      .highlighted-parent {
        flex-wrap: wrap;
      }
    }
    @media screen and (max-width: 750px) {
      .frame-parent2 {
        gap: 19px 38px;
      }
  
      .highlighted {
        padding-top: var(--padding-72xl);
        box-sizing: border-box;
        min-width: 100%;
      }
  
      .disconnected-parent {
        min-width: 100%;
      }
    }
    @media screen and (max-width: 450px) {
      .great-sound-with-container {
        font-size: var(--font-size-5xl);
        line-height: 44px;
      }
    }
</style>
  