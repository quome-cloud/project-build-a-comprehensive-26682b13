/**
 * @file Theme definitions for the application.
 */

/**
 * Represents a scale of colors.
 */
export interface ColorShades {
  [key: string]: string;
}

/**
 * Represents semantic colors with specific shades.
 */
export interface SemanticColor {
  50: string;
  500: string;
  600: string;
}

/**
 * Defines the typography styles.
 */
export interface Typography {
  fontFamily: {
    sans: string;
    serif: string;
    mono: string;
  };
  fontSize: {
    xs: string;
    sm: string;
    base: string;
    lg: string;
    xl: string;
    '2xl': string;
    '3xl': string;
    '4xl': string;
    '5xl': string;
  };
  fontWeight: {
    thin: number;
    light: number;
    normal: number;
    medium: number;
    semibold: number;
    bold: number;
    extrabold: number;
    black: number;
  } | number | string;
  lineHeight: {
    none: number;
    tight: number;
    snug: number;
    normal: number;
    relaxed: number;
    loose: number;
  };
}

/**
 * Defines spacing values.
 */
export interface Spacing {
  [key: number | string]: string;
}

/**
 * Defines border radius values.
 */
export interface BorderRadius {
  none: string;
  sm: string;
  base: string;
  md: string;
  lg: string;
  xl: string;
  '2xl': string;
  '3xl': string;
  full: string;
}

/**
 * Defines shadow styles.
 */
export interface Shadows {
  xs: string;
  sm: string;
  base: string;
  lg: string;
  xl: string;
  '2xl': string;
  inner: string;
}

/**
 * Defines the application theme.
 */
export interface Theme {
  colors: {
    primary: ColorShades;
    secondary: ColorShades;
    neutral: ColorShades;
    success: SemanticColor;
    warning: SemanticColor;
    error: SemanticColor;
    info: SemanticColor;
  };
  typography: Typography;
  spacing: Spacing;
  borderRadius: BorderRadius;
  shadows: Shadows;
  breakpoints: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    '2xl': string;
  };
  transitions: {
    none: string;
    all: string;
    default: string;
    colors: string;
    opacity: string;
    shadow: string;
    transform: string;
  };
  zIndex: {
    0: number;
    10: number;
    20: number;
    30: number;
    40: number;
    50: number;
    auto: string;
  };
}

/**
 * Theme mode options.
 */
export type ThemeMode = 'light' | 'dark' | 'system';

/**
 * Context value for theme management.
 */
export interface ThemeContextValue {
  theme: Theme;
  mode: ThemeMode;
  setMode: (mode: ThemeMode) => void;
  toggleMode: () => void;
  isDark: boolean;
}