import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

POWER_FILE = os.path.join(
    DATA_DIR,
    "電力消費_2016_2025_分析資料.csv"
)

power_df = pd.read_csv(
    POWER_FILE,
    encoding="utf-8-sig"
)
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# =========================================================
# Streamlit 基本設定
# =========================================================

st.set_page_config(
    page_title="臺灣產業結構與電力消費分析",
    page_icon="⚡",
    layout="wide"
)

POWERBI_URL = "https://app.powerbi.com/reportEmbed?reportId=d45abfdc-292f-44d9-860c-0f650c63b382&autoAuth=true&ctid=dd3d1b33-c81a-4d15-b45c-fb634e816d72"
# =========================================================
# 頁面狀態
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "首頁"


# =========================================================
# 網站標題
# =========================================================

st.title("⚡ 臺灣產業結構變遷與電力消費趨勢分析")

st.caption(
    "Taiwan Industrial Structure and Electricity Consumption Trend Analysis"
)


# =========================================================
# 導覽列
# =========================================================

nav1, nav2, nav3, nav4, nav5 = st.columns(5)


with nav1:
    if st.button("🏠 首頁", use_container_width=True):
        st.session_state.page = "首頁"


with nav2:
    if st.button("📊 Power BI 分析", use_container_width=True):
        st.session_state.page = "Power BI 分析"


with nav3:
    if st.button("🏭 產業分析", use_container_width=True):
        st.session_state.page = "產業分析"


with nav4:
    if st.button("🤖 模型驗證", use_container_width=True):
        st.session_state.page = "模型驗證"


with nav5:
    if st.button("⚡ 2026 預測", use_container_width=True):
        st.session_state.page = "2026 預測"


st.divider()


# =========================================================
# 首頁
# =========================================================

if st.session_state.page == "首頁":

    with st.container(border=True):

        st.header("從產業結構到電力需求")

        st.write(
            "本專題以 2016–2025 年資料為基礎，"
            "探討臺灣產業生產、產業結構、電力消費與氣象因素之間的關聯，"
            "並進一步利用機器學習進行電力需求預測。"
        )


    # -----------------------------------------------------
    # 專題分析架構
    # -----------------------------------------------------

    st.subheader("專題分析架構")


    col1, col2 = st.columns(2)


    with col1:

        with st.container(border=True):

            st.caption("01")

            st.subheader("⚡ 電力消費全貌")

            st.write(
                "分析 2016–2025 年臺灣整體電力消費趨勢，"
                "並觀察主要產業用電結構的變化。"
            )


    with col2:

        with st.container(border=True):

            st.caption("02")

            st.subheader("🏭 產業生產因素")

            st.write(
                "比較工業生產活動與電力消費變化，"
                "分析產業活動與用電需求之間的關聯。"
            )


    col3, col4 = st.columns(2)


    with col3:

        with st.container(border=True):

            st.caption("03")

            st.subheader("🏗️ 產業結構深入")

            st.write(
                "分析 8 大主要產業的電力消費變化，"
                "觀察電子產品及電力設備製造業等產業的用電趨勢。"
            )


    with col4:

        with st.container(border=True):

            st.caption("04")

            st.subheader("🌡️ 氣象因素比較")

            st.write(
                "將氣溫與產業生產因素進行比較，"
                "探討不同因素與電力消費之間的統計關聯。"
            )


    # -----------------------------------------------------
    # 電力需求預測
    # -----------------------------------------------------

    st.divider()

    st.subheader("電力需求預測")


    col5, col6 = st.columns(2)


    with col5:

        with st.container(border=True):

            st.caption("05")

            st.subheader("🤖 機器學習模型驗證")

            st.write(
                "使用 2016–2023 年資料建立模型，"
                "並以 2024–2025 年資料進行模型驗證。"
            )


    with col6:

        with st.container(border=True):

            st.caption("06")

            st.subheader("⚡ 2026 電力需求預測")

            st.write(
                "根據 2016–2025 年歷史電力消費資料，"
                "建立 2026 年每月電力需求預測。"
            )


    st.divider()

    st.caption(
        "資料期間：2016–2025｜預測期間：2026｜"
        "Power BI × Python × Streamlit"
    )


# =========================================================
# Power BI 分析
# =========================================================

elif st.session_state.page == "Power BI 分析":

    st.title("📊 Power BI 分析")

    st.caption(
        "2016–2025 年臺灣產業結構與電力消費分析"
    )

    st.divider()

    st.subheader("Power BI 完整分析報表")

    st.components.v1.iframe(
        POWERBI_URL,
        height=800,
        scrolling=True
    )
    # =====================================================
    # Power BI 分析總結
    # =====================================================

    st.subheader("Power BI 分析小結")

    st.success(
        "分析脈絡：電力消費趨勢 → 產業生產 → 產業結構 → "
        "產業與氣象因素比較 → 電力需求預測"
    )

# =========================================================
# 產業分析
# =========================================================

elif st.session_state.page == "產業分析":

    st.title("🏭 產業分析")
    st.caption("臺灣產業結構與電力消費變化")

    # =========================
    # 1. KPI
    # =========================
    st.subheader("關鍵指標")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        
    with kpi1:
        power_2021 = power_df.loc[
        power_df["年月"].astype(str).str[:4] == "2021",
        "電力消費"
    ].sum()

        st.metric(
        "2021 八大主要產業用電",
        f"{power_2021:,.2f}"
        )
        st.caption("百萬度")

    with kpi2:
        d2021 = power_df[
        power_df["年月"].astype(str).str[:4] == "2021"
    ]

        industry_2021 = (
        d2021.groupby("電力消費分類")["電力消費"]
        .sum()
        .sort_values(ascending=False)
    )

        main_share = industry_2021.iloc[0] / industry_2021.sum() * 100

        st.metric(
        "2021 最大用電產業",
        f"{main_share:.2f}%"
    )

        st.caption("電子產品及電力設備製造業")

    with kpi3:
        
        st.metric(
        "AI 發展相關產業用電占比",
        "23.68%"
    )
        st.caption("半導體＋資訊服務")

    with kpi4:
        st.metric(
        "2021–2025 AI相關用電變化",
        "+30.85%"
    )
        st.caption("半導體＋資訊服務")

    st.divider()

    # =========================
    # 2. 八大產業結構變化
    # =========================
    st.subheader("八大產業結構變化")

    structure_df = power_df.copy()
    structure_df["年份"] = structure_df["年月"] // 100

    structure_df = structure_df[
        structure_df["年份"].isin([2016, 2021, 2025])
    ]

    structure_df = (
        structure_df
        .groupby(["年份", "電力消費分類"])["電力消費"]
        .sum()
        .reset_index()
    )

    # 計算各產業占該年度八大產業總用電的比例
    structure_df["占比"] = (
        structure_df["電力消費"]
        / structure_df.groupby("年份")["電力消費"].transform("sum")
        * 100
    )

    # =========================
    # 橫向 100% 堆疊圖
    # =========================
    import plotly.express as px

    fig = px.bar(
        structure_df,
        y="年份",
        x="占比",
        color="電力消費分類",
        orientation="h",
        title="2016、2021、2025 八大產業用電結構",
        labels={
            "年份": "年份",
            "占比": "用電占比（%）",
            "電力消費分類": "產業"
        }
    )

    fig.update_layout(
        barmode="stack",
        xaxis=dict(
            range=[0, 100],
            ticksuffix="%"
        ),
        yaxis=dict(
            categoryorder="array",
            categoryarray=[2016, 2021, 2025]
        ),
        legend_title="八大產業"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "比較 2016、2021、2025 三個代表年份，觀察八大產業用電結構的變化。"
    )

    st.divider()
 
    # =========================
    # 3. 分析路徑
    # =========================
    st.subheader("🔎 專題分析路徑")

    step1, arrow1, step2, arrow2, step3, arrow3, step4, arrow4, step5 = st.columns(
        [1, 0.25, 1, 0.25, 1, 0.25, 1, 0.25, 1]
    )

    with step1:
        st.markdown("### ①")
        st.markdown("**電力消費**")
        st.caption("2016–2025")
        st.caption("看十年用電變化")

    with arrow1:
        st.markdown(
            "<div style='text-align:center; padding-top:32px; font-size:24px;'>→</div>",
            unsafe_allow_html=True
        )

    with step2:
        st.markdown("### ②")
        st.markdown("**高用電期間**")
        st.caption("2020–2022")
        st.caption("找關鍵高用電時期")

    with arrow2:
        st.markdown(
            "<div style='text-align:center; padding-top:32px; font-size:24px;'>→</div>",
            unsafe_allow_html=True
        )

    with step3:
        st.markdown("### ③")
        st.markdown("**產業結構**")
        st.caption("2016 → 2021 → 2025")
        st.caption("看產業結構變化")

    with arrow3:
        st.markdown(
            "<div style='text-align:center; padding-top:32px; font-size:24px;'>→</div>",
            unsafe_allow_html=True
        )

    with step4:
        st.markdown("### ④")
        st.markdown("**生產＋氣象**")
        st.caption("R² = 0.8633")
        st.caption("找用電影響因素")

    with arrow4:
        st.markdown(
            "<div style='text-align:center; padding-top:32px; font-size:24px;'>→</div>",
            unsafe_allow_html=True
        )

    with step5:
        st.markdown("### ⑤")
        st.markdown("**AI 產業**")
        st.caption("2021–2025")
        st.caption("看 AI 用電成長")

    st.divider()
    
        # =========================
    # 4. AI 相關產業
    # =========================
    st.subheader("🤖 AI 發展相關產業用電")

    # 簡短說明
    st.markdown("📌 **261 半導體製造業 × 631 資訊服務業**")

    # 讀取 AI 相關產業資料
    ai_file = os.path.join(
    DATA_DIR,
    "AI_Industry_Electricity_2021_2025.csv"
    )

    ai_df = pd.read_csv(ai_file)

    # 只保留 261 半導體製造業、631 資訊服務業
    ai_df = ai_df[
        ai_df["行業別小類"].astype(str).str.startswith(("261", "631"))
    ].copy()

    # 確保數值欄位格式正確
    ai_df["年份"] = ai_df["年份"].astype(int)
    ai_df["月份"] = ai_df["月份"].astype(int)
    ai_df["售電量"] = pd.to_numeric(
        ai_df["售電量"],
        errors="coerce"
    )

    # 年度彙整
    ai_yearly = (
        ai_df
        .groupby(["年份", "行業別小類"])["售電量"]
        .sum()
        .reset_index()
    )

    ai_yearly["產業"] = ai_yearly["行業別小類"].str.extract(
        r"^(261|631)"
    )[0]

    ai_yearly["產業"] = ai_yearly["產業"].map({
        "261": "261 半導體製造業",
        "631": "631 資訊服務業"
    })

    # =========================
    # 兩張圖同一排
    # =========================
    ai_chart1, ai_chart2 = st.columns(2)

    # 左：AI 相關產業用電趨勢
    with ai_chart1:
        st.markdown("### 📈 用電趨勢（2021–2025）")

        fig_ai_trend = px.line(
            ai_yearly,
            x="年份",
            y="售電量",
            color="產業",
            markers=True,
            title="261 vs 631"
        )

        fig_ai_trend.update_layout(
            xaxis_title="年份",
            yaxis_title="年度售電量",
            legend_title="產業"
        )

        st.plotly_chart(
            fig_ai_trend,
            use_container_width=True
        )

    # 右：AI 相關產業用電結構
    with ai_chart2:
        st.markdown("### 📊 用電結構（2021 vs 2025）")

        ai_structure = ai_yearly[
            ai_yearly["年份"].isin([2021, 2025])
        ].copy()

        fig_ai_structure = px.bar(
            ai_structure,
            x="年份",
            y="售電量",
            color="產業",
            barmode="stack",
            text_auto=".2s",
            title="2021 vs 2025"
        )

        fig_ai_structure.update_layout(
            xaxis_title="年份",
            yaxis_title="年度售電量",
            legend_title="產業"
        )

        st.plotly_chart(
            fig_ai_structure,
            use_container_width=True
        )

    # =========================
    # 重點發現
    # =========================
    st.markdown("### 🔎 重點發現")

    st.markdown(
        """
        2021–2025 年 AI 相關產業用電持續成長，其中 261 半導體製造業為主要用電來源。  
        631 資訊服務業規模較小，但亦呈現成長趨勢。
        """
    )

    st.divider()
    # =========================
    # 5. 用電高峰的背景說明
    # =========================

    st.subheader("📌 用電高峰的背景說明")

    st.markdown("""
    **2021–2022｜產業景氣與製造業需求帶動**

    經濟復甦、台商回流，以及半導體、電子零組件等產業需求增加，
    帶動工業生產與用電成長。2022 年尖峰負載更突破 4,000 萬瓩。

    **2023｜全球景氣降溫**

    全球景氣走緩、庫存調整，使工業生產及工業用電下降，
    全台用電量也較前一年回落。

    **2024–2025｜AI 與半導體需求支撐**

    AI、新興科技及半導體相關產業需求持續，使高科技產業用電維持高檔；
    雖然傳統產業景氣、節能及氣候因素造成部分抵銷，
    整體用電仍維持在較高水準。
    """)

    st.caption("資料來源：經濟部能源署、台灣電力公司公開資料")

    st.markdown("### 🔎 小結")

    st.markdown("""
    從本專題的資料分析與官方資料可以看出，
    **產業生產活動是台灣用電變化的重要背景因素，氣候則是另一項影響因素。**

    因此，下一步將進一步檢視模型對用電變化的**解釋能力與預測表現**，
    並觀察 **2026 年預測與實際用電的差異**。
    """)

    st.divider()
# =========================================================
# 模型驗證
# =========================================================

# =========================================================
# 模型驗證
# =========================================================

elif st.session_state.page == "模型驗證":

    st.title("🤖 模型驗證")

    st.markdown(
        """
        **模型建立：2016–2025 年共 10 年月資料**
        
        **模型驗證：2024–2025 年資料**
        """
    )

    # =====================================================
    # 模型評估指標
    # =====================================================

    st.subheader("模型評估結果")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "MAE",
            "673.15",
            "百萬度"
        )

    with col2:
        st.metric(
            "RMSE",
            "795.07",
            "百萬度"
        )

    with col3:
        st.metric(
            "R²",
            "0.8633"
        )

    # =====================================================
    # 模型驗證結果說明
    # =====================================================

    st.markdown(
        """
        ### 模型驗證結果

        R² = 0.8633，表示模型可解釋約 **86.33% 的用電變化**；
        MAE 與 RMSE 用於衡量預測誤差。
        從 2024–2025 年實際值與預測值的比較來看，
        模型能掌握整體用電趨勢，具備進一步進行
        **2026 年用電預測**的基礎。
        """
    )

    st.divider()

    # =====================================================
    # 讀取 2024–2025 模型驗證資料
    # =====================================================

    validation_file = os.path.join(
    DATA_DIR,
    "Electricity_Prediction_2024_2025.csv"
    )

    validation = pd.read_csv(
        validation_file,
        encoding="utf-8-sig"
    )

    validation["日期"] = pd.to_datetime(
        validation["年月"].astype(str),
        format="%Y%m"
    )

    # =====================================================
    # 實際值 vs 模型預測
    # =====================================================

    st.subheader("2024–2025 實際值與模型預測")

    fig, ax = plt.subplots(figsize=(10, 4.8))

    ax.plot(
        validation["日期"],
        validation["電力消費_總計(數值)"],
        marker="o",
        label="實際電力消費"
    )

    ax.plot(
        validation["日期"],
        validation["預測電力消費"],
        marker="o",
        label="模型預測"
    )

    ax.set_title(
        "2024–2025 實際電力消費與模型預測"
    )

    ax.set_xlabel("月份")

    ax.set_ylabel(
        "電力消費（百萬度）"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    # =====================================================
    # 預測資料表
    # =====================================================

    st.subheader("模型預測資料")

    display_df = validation[
        [
            "年月",
            "電力消費_總計(數值)",
            "預測電力消費",
            "預測誤差"
        ]
    ].copy()

    display_df.columns = [
        "年月",
        "實際電力消費",
        "預測電力消費",
        "預測誤差"
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.info(
        "2024–2025 年資料作為測試資料，"
        "用於檢驗模型對已知資料的預測表現。"
    )

# =========================================================
# 2026 預測
# =========================================================

elif st.session_state.page == "2026 預測":

    st.title("⚡ 2026 年電力需求預測")

    st.markdown(
        """
        **模型建立：2016–2025 年共 10 年月資料**

        **預測期間：2026 年 1–12 月**
        """
    )

    # -----------------------------------------------------
    # 讀取 2026 預測資料
    # -----------------------------------------------------

    forecast_file = os.path.join(
    DATA_DIR,
    "Electricity_Prediction_2026.csv"
    )
    df = pd.read_csv(
        forecast_file,
        encoding="utf-8-sig"
    )

    df["年月"] = df["年月"].astype(str)

    df["預測電力消費"] = pd.to_numeric(
        df["預測電力消費"],
        errors="coerce"
    )

    # -----------------------------------------------------
    # 左側：月份選擇
    # 右側：2026 預測折線圖
    # -----------------------------------------------------

    col1, col2 = st.columns([1, 3])

    with col1:

        st.subheader("🔽 選擇預測月份")

        month = st.selectbox(
            "月份",
            df["年月"].tolist(),
            label_visibility="collapsed"
        )

        selected = df[
            df["年月"] == month
        ].iloc[0]

        st.metric(
            "預測電力消費",
            f"{selected['預測電力消費']:,.0f} 百萬度"
        )

    with col2:

        st.subheader("2026 年每月電力需求預測")

        # -------------------------------------------------
        # Matplotlib 折線圖
        # -------------------------------------------------

        fig, ax = plt.subplots(figsize=(10, 4.5))

        ax.plot(
            df["年月"],
            df["預測電力消費"],
            marker="o"
        )

        ax.set_title(
            "2026 年每月電力需求預測"
        )

        ax.set_xlabel("月份")

        ax.set_ylabel(
            "電力消費（百萬度）"
        )

        # Y 軸範圍
        y_min = 19000
        y_max = 28000

        ax.set_ylim(
            y_min,
            y_max
        )

        # Y 軸每 1,000 一格
        ax.set_yticks(
            range(
                y_min,
                y_max + 1,
                1000
            )
        )

        ax.grid(
            True,
            alpha=0.3
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig)

        plt.close(fig)

    # =====================================================
    # 2026 預測 vs 實際
    # =====================================================

    st.divider()

    st.subheader("📊 2026 年預測與實際用電比較")

    # -----------------------------------------------------
    # 讀取 2026 實際電力消費資料
    # -----------------------------------------------------

    actual_file = os.path.join(
    DATA_DIR,
    "電力消費月資料(2018年後)(11507).csv"
    )

    actual_df = pd.read_csv(
        actual_file,
        encoding="utf-8-sig"
    )

    # -----------------------------------------------------
    # 整理實際資料日期
    # -----------------------------------------------------

    actual_df["日期(年/月)"] = (
        actual_df["日期(年/月)"]
        .astype(str)
        .str.strip()
    )

    actual_df["年月"] = (
        actual_df["日期(年/月)"]
        .str.replace(r"\D", "", regex=True)
        .str[:6]
    )

    actual_df["電力消費_總計(數值)"] = pd.to_numeric(
        actual_df["電力消費_總計(數值)"],
        errors="coerce"
    )

    # 只保留 2026 年實際資料
    actual_2026 = actual_df[
        actual_df["年月"].str.startswith("2026")
    ].copy()

    # -----------------------------------------------------
    # 預測資料與實際資料依年月合併
    # -----------------------------------------------------

    compare_df = pd.merge(
        df[
            [
                "年月",
                "預測電力消費"
            ]
        ],
        actual_2026[
            [
                "年月",
                "電力消費_總計(數值)"
            ]
        ],
        on="年月",
        how="inner"
    )

    compare_df = compare_df.rename(
        columns={
            "電力消費_總計(數值)": "實際電力消費"
        }
    )

    # -----------------------------------------------------
    # 計算預測誤差
    # -----------------------------------------------------

    compare_df["預測誤差"] = (
        compare_df["實際電力消費"]
        - compare_df["預測電力消費"]
    )

    compare_df["絕對誤差"] = (
        compare_df["預測誤差"]
        .abs()
    )

    # -----------------------------------------------------
    # 預測 vs 實際折線圖
    # -----------------------------------------------------

    if not compare_df.empty:

        fig_compare, ax_compare = plt.subplots(
            figsize=(10, 4.8)
        )

        # -------------------------------------------------
        # 預測線：完整顯示 2026/01–2026/12
        # -------------------------------------------------

        ax_compare.plot(
            df["年月"],
            df["預測電力消費"],
            marker="o",
            label="模型預測"
        )

        # -------------------------------------------------
        # 實際線：只顯示目前已有的實際資料
        # -------------------------------------------------

        ax_compare.plot(
            compare_df["年月"],
            compare_df["實際電力消費"],
            marker="o",
            label="實際電力消費"
        )

        ax_compare.set_title(
            "2026 年實際電力消費與模型預測比較"
        )

        ax_compare.set_xlabel("月份")

        ax_compare.set_ylabel(
            "電力消費（百萬度）"
        )

        ax_compare.set_ylim(
            y_min,
            y_max
        )

        ax_compare.set_yticks(
            range(
                y_min,
                y_max + 1,
                1000
            )
        )

        ax_compare.grid(
            True,
            alpha=0.3
        )

        ax_compare.legend()

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig_compare)

        plt.close(fig)

        # -------------------------------------------------
        # 目前已知月份的預測誤差
        # -------------------------------------------------

        mae_2026 = (
            compare_df["絕對誤差"]
            .mean()
        )

        actual_months = len(
            compare_df
        )

        st.markdown(
            f"""
            ### 🔎 目前預測結果

            截至目前已有實際資料的 **{actual_months} 個月份**，
            模型預測與實際用電可以進行比較。

            目前已知月份的平均絕對誤差（MAE）為
            **{mae_2026:,.2f} 百萬度**。

            這項比較可用來觀察模型在 **2026 年實際資料**
            出現後的預測表現，並作為本專題模型預測能力的延伸驗證。
            """
        )

    else:

        st.info(
            "目前尚未找到可與 2026 年預測資料對應的實際用電月份。"
        )

    # -----------------------------------------------------
    # 2026 預測資料表
    # -----------------------------------------------------

    st.divider()

    st.subheader("📋 2026 年預測資料")

    table_col1, table_col2, table_col3 = st.columns(
        [1, 2, 1]
    )

    with table_col2:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )