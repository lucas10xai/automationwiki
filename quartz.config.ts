import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "10XAI Notes",  // 🔧 BRANDING: Tên hiển thị trên tab trình duyệt
    pageTitleSuffix: " · 10XAI",  // 🔧 BRANDING: Suffix mỗi trang — "Tên Trang · 10XAI"
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
      // 🔧 ANALYTICS: Đổi thành "google" + tagId nếu dùng GA4
      // provider: "google",
      // tagId: "G-XXXXXXXXXX",
    },
    locale: "vi-VN",  // 🔧 LOCALE: Tiếng Việt
    baseUrl: "notes.10xai.top",  // 🔧 DOMAIN: Public URL của bạn
    ignorePatterns: ["private", "templates", ".obsidian", "_archive", "_drafts"],  // 🔧 PRIVACY: Thư mục không publish
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        // 🔧 TYPOGRAPHY: Bộ font tối giản, chuyên nghiệp cho thương hiệu 10XAI
        header: "Inter",          // Modern, clean — dùng cho heading
        body: "Inter",            // Nhất quán với header
        code: "JetBrains Mono",   // Developer-friendly monospace
      },
      colors: {
        // 🔧 COLORS LIGHT MODE — Tối giản, nền trắng tinh tế
        lightMode: {
          light: "#f8f9fa",          // Nền trang
          lightgray: "#e9ecef",      // Đường kẻ, border
          gray: "#adb5bd",           // Text phụ, placeholder
          darkgray: "#343a40",       // Text chính
          dark: "#212529",           // Heading, bold
          secondary: "#0066cc",      // Link, accent chính — xanh 10XAI
          tertiary: "#00b4d8",       // Hover, highlight nhẹ
          highlight: "rgba(0, 102, 204, 0.08)",
          textHighlight: "#caf0f888",
        },
        // 🔧 COLORS DARK MODE — Nền tối chuyên nghiệp
        darkMode: {
          light: "#0d1117",          // Nền trang — GitHub dark
          lightgray: "#21262d",      // Card, sidebar background
          gray: "#484f58",           // Border, divider
          darkgray: "#c9d1d9",       // Text thường
          dark: "#f0f6fc",           // Heading, bold text
          secondary: "#58a6ff",      // Link, accent — xanh sáng
          tertiary: "#79c0ff",       // Hover effect
          highlight: "rgba(88, 166, 255, 0.1)",
          textHighlight: "#003d6b88",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
